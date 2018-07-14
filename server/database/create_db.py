import pandas as pd
import sqlite3

import mysql.connector as mc
import config


def get_sqlite_conn():
    return sqlite3.connect(config.db_name)


def get_mysql_conn():
    return mc.connect(user=config.mysql_user,
                      password=config.mysql_pass,
                      host=config.mysql_host,
                      database=config.mysql_db)


def create_patients_table(conn):
    patients_df = pd.read_excel(config.patients_data_file)

    patients_df.to_sql(name=config.patients_table_name, con=conn, if_exists='replace', index=False)


def create_schedule_table(conn):
    sched_df = pd.read_excel(config.schedule_data_file)

    sched_df.to_sql(config.schedule_table_name, conn, if_exists='replace', index=False)


def create_vaccine_logic_table(conn):
    vacc_df = pd.read_excel(config.vaccine_logic_file)

    vacc_df.rename(columns={
                            'ID': 'demo_id',
                            'Vaccine': 'vaccine_name',
                            'Recommendation': 'recommendation_text'
                            },
                   inplace=True)

    vacc_df.to_sql(config.vaccine_logic_table_name, conn, if_exists='replace', index=False)


def create_vaccine_demos_table(conn):
    vacc_demos_df = pd.read_excel(config.vaccine_demos_file)

    vacc_demos_df.rename(columns={
                            'ID': 'demo_id',
                            'Sex (0=man 1 = women)': 'sex',
                            'Age (0= <26, 1 =27-61, 2= 62-64 3= >65)': 'age_bin',
                            'Pregnant': 'is_pregnant',
                            'Vaccine Hesitancy': 'is_vaccine_hesitant'
                            },
                         inplace=True)

    vacc_demos_df.to_sql(config.vaccine_demos_table_name, conn, if_exists='replace', index=False)


def get_family_id(conn, first_name, last_name):
    query = "SELECT family_id FROM patients WHERE first_name = '%s' AND last_name = '%s'" % (first_name, last_name)
    df = pd.read_sql(query, conn)
    n_results = df.shape[0]

    if n_results == 0:
        raise ValueError("%s %s not found in DB" % (first_name, last_name))

    if n_results > 1:
        raise ValueError("%s %s not found in DB" % (first_name, last_name))

    return df.family_id[0]


def get_patient_id(conn, first_name, last_name):
    query = "SELECT patient_id FROM patients WHERE first_name = '%s' AND last_name = '%s'" % (first_name, last_name)
    df = pd.read_sql(query, conn)
    n_results = df.shape[0]

    if n_results == 0:
        raise ValueError("%s %s not found in DB" % (first_name, last_name))

    if n_results > 1:
        raise ValueError("%s %s not found in DB" % (first_name, last_name))

    return df.patient_id[0]


def get_all_recommendations(conn, first_name, last_name):
    """

    :param first_name: patient first name
    :param conn: database connection
    :param last_name: patient last name
    :param requested_date: date desired
    :param requested_time: start time of the 30-min timeslot desired
    :return: df containing results
    """

    query = """
    SELECT
      p.first_name,
      p.last_name,
      v.vaccine_name,
      v.recommendation_text
      FROM patients p
       JOIN demos d
        ON
         (p.current_age_bin = d.age_bin)
         AND
         (p.sex = d.sex)
         AND
         (p.is_known_pregnant = d.is_pregnant)
       JOIN vaccine_recommendations v
        ON
         (d.demo_id = v.demo_id)
      WHERE
       family_id = (SELECT family_id
                    FROM patients
                    WHERE first_name = '%s' AND last_name = '%s')
       AND
       is_vaccine_hesitant = 0;
    """ % (first_name, last_name)

    df = pd.read_sql(query, conn)
    n_results = df.shape[0]

    if n_results == 0:
        raise ValueError("No recommended results found in DB")

    return df


if __name__ == '__main__':
    connection = get_sqlite_conn()
    create_patients_table(connection)
    create_schedule_table(connection)
    create_vaccine_logic_table(connection)
    create_vaccine_demos_table(connection)

    print(get_all_recommendations(connection, 'Abhi', 'Patel').head())
    print(get_all_recommendations(connection, 'John', 'Doe').head())

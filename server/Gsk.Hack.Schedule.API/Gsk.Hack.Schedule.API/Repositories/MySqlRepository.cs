using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Gsk.Hack.Schedule.API.Repositories
{
    public class MySqlRepository
    {
        private const string ConnectionString =
            "Server=gskdbserverimnno.mysql.database.azure.com; Port=3306; Database=vaccine; Uid=gskadmin@gskdbserverimnno; Pwd=ImmunoH@CK1;";

        public MySqlRepository()
        {
            
        }

        public void GetVaccines(string name)
        {
            MySqlConnection conn = new MySqlConnection(ConnectionString);
            conn.Open();
            string sql = "SELECT * FROM TEST";
            //string sql = "SELECT * FROM TEST WHERE Name='@Name'";
            MySqlCommand cmd = new MySqlCommand(sql, conn);
            //cmd.Parameters.AddWithValue("@Name", name);


            MySqlDataReader rdr = cmd.ExecuteReader();
            while (rdr.Read())
            {
                Console.WriteLine(rdr[0] + " -- " + rdr[1]);
            }
            rdr.Close();
        }
    }
}
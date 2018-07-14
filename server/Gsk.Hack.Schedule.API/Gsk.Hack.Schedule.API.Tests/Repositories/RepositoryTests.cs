using Gsk.Hack.Schedule.API.Repositories;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Gsk.Hack.Schedule.API.Tests.Repositories
{
    [TestClass]
    public class RepositoryTests
    {
        [TestMethod]
        public void GetVaccines_ReadsFromTestTable_ShouldSucceed()
        {
            MySqlRepository repository = new MySqlRepository();
            repository.GetVaccines("Pat");
        }
    }
}

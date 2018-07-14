using System.Web;
using System.Web.Mvc;

namespace Gsk.Hack.Schedule.API
{
    public class FilterConfig
    {
        public static void RegisterGlobalFilters(GlobalFilterCollection filters)
        {
            filters.Add(new HandleErrorAttribute());
        }
    }
}

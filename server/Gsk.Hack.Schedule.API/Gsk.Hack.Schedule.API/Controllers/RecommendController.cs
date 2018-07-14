using Gsk.Hack.Schedule.API.Models;
using System;
using System.Web.Http;

namespace Gsk.Hack.Schedule.API.Controllers
{
    [RoutePrefix("api/schedule")]
    public class ScheduleController : ApiController
    {
        [HttpPost]
        [Route("recommend")]
        public IHttpActionResult Recommend(RecommendRequest request)
        {
            DateTime appointmentTime;

            if (DateTime.TryParse(request.ApointmentTime, out appointmentTime))
            {
                return Ok(request.CallerName + " made an appointment for " + request.PatientName + " at " 
                + appointmentTime.Hour + " O'Clock on " +
                appointmentTime.DayOfWeek + " " + appointmentTime.Month + " " + appointmentTime.Day);
            }
            else
            {
                return BadRequest("Could not parse date time");
            }  
        }
    }
}
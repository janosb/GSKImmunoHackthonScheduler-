using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Gsk.Hack.Schedule.API.Models
{
    public class RecommendRequest
    {
        public string CallerName { get; set; }
        public string PatientName { get; set; }
        public string ApointmentTime { get; set; }
    }
}
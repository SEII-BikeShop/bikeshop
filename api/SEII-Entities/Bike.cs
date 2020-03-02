using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Threading.Tasks;

namespace BikeShopAnalyticsAPI.Models.Entities
{
    public class Bike
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int BikeID { get; set; }

        public string Name { get; set; }

        public decimal SalesPrice { get; set; }

        /*  To be added later.
        public ModelType Type { get; set; }
        public Color Color { get; set; }
        */
    }
}

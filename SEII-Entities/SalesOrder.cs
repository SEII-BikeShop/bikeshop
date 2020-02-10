using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Threading.Tasks;

namespace BikeShopAnalyticsAPI.Models.Entities
{
    public class SalesOrder
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int SalesID { get; set; }

        [ForeignKey("Bike")]
        public int BikeID { get; set; }

        public decimal SalesPrice { get; set; }

        public decimal Tax { get; set; }

        public decimal Discount { get; set; }

        public DateTime Date { get; set; }

        public string State { get; set; }

        public int Units { get; set; }


        /*  To be added later.
        [ForeignKey("Customer")]
        public int CustomerID { get; set; }

        [ForeignKey("Employee")]
        public int EmployeeID { get; set; }
        
        [ForeignKey("Store")]
        public int StoreID { get; set; }

        */

        public virtual Bike Bike { get; set; }
        
        /*  TO be added later.
        public virtual Customer Customer { get; set; }
        public virtual Employee Employee { get; set; }
        public virtual Store Store { get; set; }
        */


    }
}

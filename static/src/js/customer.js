console.log('snippet')
odoo.define('top_customers.dynamic', function (require) {
   var PublicWidget = require('web.public.widget');
   console.log(PublicWidget,'public')
   var rpc = require('web.rpc');
   var core = require('web.core');
   var Qweb = core.qweb;
   var Dynamic = PublicWidget.Widget.extend({
       selector: '.dynamic_snippet_blog',
       start: function () {
           var self = this;
           console.log(self,'23456')
           rpc.query({
               route: '/customer/top',
               params: {},
           }).then(function (result) {
               result[0].set_active=true;
               $('.qweb_customer').append(Qweb.render('top_customers.customer_template',{result}));
           });
       },
   });

   PublicWidget.registry.dynamic_snippet_blog = Dynamic;
   return Dynamic;
});
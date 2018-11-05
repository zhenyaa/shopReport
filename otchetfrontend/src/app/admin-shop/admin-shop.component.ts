import { Component, OnInit } from '@angular/core';
import {APIService} from '../api.service';
interface Opera{
	name:string;
};
@Component({
  selector: 'app-admin-shop',
  templateUrl: './admin-shop.component.html',
  styleUrls: ['./admin-shop.component.css']
})
export class AdminShopComponent implements OnInit {
panelOpenState = false;
public  operation:  Array<object> = [];
 operation2: Opera = {
	name : "",
};

  constructor(public  apiService:  APIService) { }

  ngOnInit() {
  	this.getShop();
  }

   public  getShop(){
    this.apiService.getShop().subscribe((data:  Array<object>) => {
        this.operation  =  data;
        console.log(data);
    });
    console.log(this.operation)
};

createShop(){
const operation1  = {sum: 200,name: "optima"};
this.apiService.createShop(this.operation2).subscribe((response) => {
    console.log(response);
});
this.panelOpenState = true;
this.getShop();
};

}

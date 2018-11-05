import { Component, OnInit } from '@angular/core';
import {APIService} from '../api.service';
interface Opera{
	name:string;
	sum:number;

};

@Component({
  selector: 'app-pay-report',
  templateUrl: './pay-report.component.html',
  styleUrls: ['./pay-report.component.css']
})


export class PayReportComponent implements OnInit {
panelOpenState1 = true;
panelOpenState2 = false;
public  operation:  Array<object> = [];
 operation2: Opera = {
	name : "",
	sum : null,

};
  constructor(private  apiService:  APIService) { }

  ngOnInit() {
  	 this.getContacts();
  }
  public  getContacts(){
    this.apiService.getContacts({day:"today", thisUser: true}).subscribe((data:  Array<object>) => {
        this.operation  =  data;
        console.log(data);
    });
    console.log(this.operation)
};



createContact(){
const operation1  = {sum: 200,name: "optima"};
this.panelOpenState2 = true;
this.apiService.createContact(this.operation2).subscribe((response) => {
    console.log(response);
});
this.getContacts();
this.operation2 = {name :"", sum: null}
};
}

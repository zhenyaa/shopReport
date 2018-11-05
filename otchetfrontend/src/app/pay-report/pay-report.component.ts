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
public  emitent:  Array<object> = [];
public  operation:  Array<object> = [];
 operation2: Opera = {
	name : "",
	sum : null,

};
  constructor(private  apiService:  APIService) { }

  ngOnInit() {
  	 this.getContacts();
     this.getEmitent();
  }
  public  getContacts(){
    this.apiService.getContacts({day:"today", thisUser: true}).subscribe((data:  Array<object>) => {
        this.operation  =  data;
        console.log(data);
    });
    console.log(this.operation)
};

  getEmitent(){
    this.apiService.getEmitentAll().subscribe((data:  Array<object>) => {
           this.emitent  = data;
           console.log('its emitent',data);
      });
  }



createContact(){
  console.log(this.operation2)
this.panelOpenState2 = true;
this.apiService.createContact(this.operation2).subscribe((response) => {
    console.log(response);
});
this.getContacts();
this.operation2 = {name :"", sum: null}
};
}

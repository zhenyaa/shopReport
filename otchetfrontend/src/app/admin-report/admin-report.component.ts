import { Component, OnInit} from '@angular/core';
import {FormControl} from '@angular/forms';
import {TooltipPosition} from '@angular/material';
import {APIService} from '../api.service';
import {MyfilterPipe} from './myfilter.pipe'
interface adminRequst{
	shop:string,
	shopDesk:number,
  inctitle:string,
	dateStart:string,
	dateEnd:string,
};
interface adminDate{
  dateStart:Date,
  dateEnd:Date,
}
@Component({
  selector: 'app-admin-report',
  templateUrl: './admin-report.component.html',
  styleUrls: ['./admin-report.component.css']
})
export class AdminReportComponent implements OnInit {
    public  shops:  Array<object> = [];
    public  userShop:  Array<object> = [];
    public  userShopWeve:  Array<object> = [];
    public title:  Array<object> = [];
    public titleViwe:  Array<object> = [];
    public tdata:  Array<object> = [];
    displayedColumns: string[] = ['Магазин', 'Касса', 'morningR', 'tsum', 'erd', 'erc','ern','err', 'erdate','test', 'test2', 'test3'];
// ,'morningR', 'tsum', 'err', 'erc', 'ern'
 adminrequste:adminRequst ={
	shop:null,
	shopDesk:null,
  inctitle:null,
	dateStart:null,
	dateEnd:null,
};
 admindate:adminDate ={
  dateStart:new Date(),
  dateEnd:new Date(),
};
filter1 = {'shopname': 'apteka1'}
  constructor(public  apiService:  APIService) { }

  ngOnInit() {
    this.getShop();
    this.getWorkPlace();
    this.getIncTitle();
  }

  sendRequstAdmin(){
  	console.log(this.adminrequste);
    this.adminrequste.dateStart=this.admindate.dateStart.toDateString();
    this.adminrequste.dateEnd=this.admindate.dateEnd.toDateString();
    this.apiService.getAdminReport(this.adminrequste).subscribe((data:  Array<object>) => {
      this.tdata = data
    console.log(data);
});
  }

  getIncTitle(){
    this.apiService.getOperationAll().subscribe((data:  Array<object>) => {
           this.title  =  this.titleViwe =  data;
           console.log('its title',data);
      });
  }

  getShop(){
      this.apiService.getShop().subscribe((data:  Array<object>) => {
           this.shops  = data;
           console.log('its shop',data);
      });
  }
  test($event){
    this.userShopWeve = this.userShop.filter(test => {
       return test["shopname"] === $event;
    });

  }

   filterTitle($event){
    this.titleViwe = this.title
    .filter(filterTitle => {
       return filterTitle["placename"] === $event;
    });
    console.log(this.titleViwe)
  }

  getWorkPlace(){
    this.apiService.getUserAll().subscribe((data:  Array<object>) => {
           this.userShop  =  data;
           console.log(data);
           console.log('its user oll',this.userShop);
           console.log('its user oll',this.shops);
           
      });
  }

  xerq(t) {
    console.log('xerq' ,t);
  }
}

import { Component, OnInit, Renderer2} from '@angular/core';
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
  styleUrls: ['./admin-report.component.css'],
})
export class AdminReportComponent implements OnInit {
    public  shops:  Array<object> = [];
    public  userShop:  Array<object> = [];
    public  userShopWeve:  Array<object> = [];
    public title:  Array<object> = [];
    public titleViwe:  Array<object> = [];
    public tdata:  Array<object> = [];
    public executeDate:  Array<object> = [];
    displayedColumns: string[] = ['Магазин', 'Касса', 'morningR', 'tsum', 'erd', 'erc','ern','err', 'erdate','test', 'test2', 'test3', 'but'];
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

  constructor(public  apiService:  APIService, private   renderer:Renderer2) { }

  ngOnInit() {
    this.getShop();
    this.getWorkPlace();
    this.getIncTitle();
    this.getExecuteDate();
  }


  sendRequstAdmin(){
    console.log(this.adminrequste);
    this.adminrequste.dateStart=this.admindate.dateStart.toDateString();
    this.adminrequste.dateEnd=this.admindate.dateEnd.toDateString();
    this.apiService.getAdminReport(this.adminrequste).subscribe((data:  Array<object>) => {
      this.tdata = data.sort((a,b) => new Date(a["erdate"]).getDate() - new Date(b["erdate"]).getDate())
    console.log('its for cheked',data);
},
err => {
  if (err.status ==401){
      // console.log("status 401 error autentification")
  }
});
// err=> console.log("error", err.status));
  }

  getIncTitle(){
    this.apiService.getOperationAll().subscribe((data:  Array<object>) => {
           this.title  =  this.titleViwe =  data;
           //console.log('its title',data);
      });
  }

  getExecuteDate(){
    this.apiService.getExecuteMoneyDate().subscribe((data:  Array<object>) => {
           this.executeDate  = data;
           //console.log('its execute date',data);
      });
  }

  dateClass = (d: Date) => {
    const date = d.getDate();

    // Highlight the 1st and 20th day of each month.
    return (date === 1 || date === 20) ? 'example-custom-date-class' : undefined;
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

  coloredRow(event){
    //console.log(this.executeDate["Idate"])
    if (this.executeDate.map(t => t["Idate"]).includes(event)){
     //console.log('2 param ',this.executeDate,event )
      return true;
    }
    else{
    return false;}
  }
  watchchange(row){
    console.log("work chaked",row);
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

   getTotalCost() {
    //<td mat-cell *matCellDef="let tdata"> {{((tdata.morningR + tdata.erc) - tdata.tsum) - tdata.erd - tdata.ern | number: '.2' }} </td>
    // return this.tdata.map(t => t).reduce((acc, value) => acc + value.morningR + value.erc- value.tsum-value.erd- value.ern, 0);
    return this.tdata.reduce((acc, value) => acc + value['morningR']+ value['erc'] - value['tsum']- value['erd']- value['ern'], 0);
  }

  getTotalmorningR(){
        return this.tdata.reduce((acc, value) => acc + value['morningR'], 0);
  }
  getTotaltsum(){
            return this.tdata.reduce((acc, value) => acc + value['tsum'], 0);
  }

  getTotalerd(){
                return this.tdata.reduce((acc, value) => acc + value['erd'], 0);
  }
  getTotalerc(){
                    return this.tdata.reduce((acc, value) => acc + value['erc'], 0);
  }
  getTotalern(){
    return this.tdata.reduce((acc, value) => acc + value['ern'], 0);
  }
  getTotalerr(){
    return this.tdata.reduce((acc, value) => acc + value['err'], 0);
  }
  getTotalTest(){
    return this.tdata.reduce((acc, value) => acc + value['morningR']+ value['erc'] - value['ern'], 0);
  }

  adminresetLabel(row){
 let mask = row;
    mask["Mstate"] = false;
    let foundIndex = this.tdata.findIndex(x => x['Mid'] === row['Mid'])
    this.tdata[foundIndex] = mask;

    this.apiService.addAdminLabel({id:row["Mid"], state: false}).subscribe((data:  Array<object>) => {
           console.log(data);
      });
  }
  adminaddLabel(row){
    let mask = row;
    mask["Mstate"] = true;
    let foundIndex = this.tdata.findIndex(x => x['Mid'] === row['Mid'])
    this.tdata[foundIndex] = mask;
      this.apiService.addAdminLabel({id:row["Mid"], state: true}).subscribe((data:  Array<object>) => {
           console.log(data);
      });

  }
}

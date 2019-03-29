import { Component, OnInit } from '@angular/core';
import { Chart } from 'chart.js';
import {DashbordApiService} from '../dashbord-api.service'
 // import 'rxjs/add/operator/map';
 // import { map } from 'rxjs/operators';
 import {catchError} from "rxjs/operators";


@Component({
  selector: 'app-radar-chrts',
  templateUrl: './radar-chrts.component.html',
  styleUrls: ['./radar-chrts.component.css']
})
export class RadarChrtsComponent implements OnInit {
  public pieChartLabels = [];
  public pieChartData = [];
  public pieChartType = 'pie';
  showPie:boolean = false;
  constructor(public  dashApiService:  DashbordApiService) { }

  ngOnInit() {
  	this.dashApiService.getSumForRadar().subscribe((res: Array<any>) =>{
  		// {this.pieChartLabels, this.pieChartData} = res.map(res => {res.name, res.sum});
  		this.pieChartLabels = res.map(res => res.name)
  		this.pieChartData = res.map(res=> res.sum)
  		console.log('test', res);
  		this.showPie = true;
  		// console.log(this.pieChartData, this.pieChartLabels)
  	})
  }
}

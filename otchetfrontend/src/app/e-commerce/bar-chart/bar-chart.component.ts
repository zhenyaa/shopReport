import { Component, OnInit } from '@angular/core';
import {DashbordApiService} from '../dashbord-api.service'
@Component({
  selector: 'app-bar-chart',
  templateUrl: './bar-chart.component.html',
  styleUrls: ['./bar-chart.component.css']
})
export class BarChartComponent implements OnInit {

  constructor(public  dashApiService:  DashbordApiService) { }
showbord: boolean = false;
  ngOnInit() {
  	this.dashApiService.getSumForChart().subscribe((res: Array<any>) =>{
  		console.log(res)
  		this.chartData =res["point"];
  		this.chartLabels = res['day']
  		this.showbord = true;
  	})
  }

   public chartOptions = {
    // scaleShowVerticalLines: true,
    responsive: true
  };
  // public chartLabels = ['ПОН', 'ВТОР', 'СРЕД', 'ЧЕТ', 'ПЯТН', 'СУБОТ', 'ВОСКРЕ'];
  public chartLabels = [];
  public barChartType = 'bar';
  public barChartLegend = true;
  public chartData  = [
    // {data: [65, 59, 80, 81, 56, 55, 40], label: 'Аптека'},
    // {data: [45, 67, 23, 11, 22, 45, 22], label: 'Аптека'},
    // {data: [28, 34, 54, 21, 58, 32, 45], label: 'Деликат'},
    // // {data: [45, 67, 23, 11, 22, 45, 22], label: 'ДеликатC'},
    // {data: [12, 54, 43, 23, 76, 21, 32], label: 'Foto'}
  ];

}

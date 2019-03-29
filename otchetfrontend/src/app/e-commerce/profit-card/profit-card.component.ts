import { Component, OnInit } from '@angular/core';
import {DashbordApiService} from '../dashbord-api.service'
@Component({
  selector: 'app-profit-card',
  templateUrl: './profit-card.component.html',
  styleUrls: ['./profit-card.component.css']
})
export class ProfitCardComponent implements OnInit {
summ:number = 0
  constructor(public  dashApiService:  DashbordApiService) { }

  ngOnInit() {
  	this.dashApiService.getSumProfit().subscribe(res => this.summ = res['summ'])
  }

}

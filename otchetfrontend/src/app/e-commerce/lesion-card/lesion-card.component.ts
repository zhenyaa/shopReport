import { Component, OnInit } from '@angular/core';
import {DashbordApiService} from '../dashbord-api.service'

@Component({
  selector: 'app-lesion-card',
  templateUrl: './lesion-card.component.html',
  styleUrls: ['./lesion-card.component.css']
})
export class LesionCardComponent implements OnInit {
summInc:number = 0
  constructor(public  dashApiService:  DashbordApiService) { }

  ngOnInit() {
  	this.dashApiService.getSumInc().subscribe(res => {
  		this.summInc = res['incsumm']
  		console.log(res)})
  }

}

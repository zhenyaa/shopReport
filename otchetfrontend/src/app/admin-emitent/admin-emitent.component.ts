import { Component, OnInit } from '@angular/core';
import {APIService} from '../api.service';

export interface Emitent {
  name: string;
}
@Component({
  selector: 'app-admin-emitent',
  templateUrl: './admin-emitent.component.html',
  styleUrls: ['./admin-emitent.component.css']
})
export class AdminEmitentComponent implements OnInit {
	userPanel = false;
 public  emi:  Array<object> = [];
  emitent: Emitent = {
  name: null
  };
  constructor(public  apiService:  APIService) { }

  ngOnInit() {
  	this.getEmitent();
  }

 getEmitent(){
      this.apiService.getEmitentAll().subscribe((data:  Array<object>) => {
           this.emi  = data;
           console.log('its emitent',data);
      });
  }

 createEmitent(){
 	console.log(this.emitent)
		this.apiService.createEmitent(JSON.stringify(this.emitent)).subscribe((response) => {
    		console.log(response);
				});
		this.getEmitent();
  	this.userPanel = true;
  	this.emitent = {name:null};
	
 }
}

import { Component, OnInit } from '@angular/core';
import {APIService} from '../api.service';
import { FormsModule } from '@angular/forms';
export interface User {
  shopname: string;
  username: string;
  pass: string;
}
@Component({
  selector: 'app-admin-user',
  templateUrl: './admin-user.component.html',
  styleUrls: ['./admin-user.component.css']
})
export class AdminUserComponent implements OnInit {
	userPanel = false;
	public  shops:  Array<object> = [];
	public  userShop:  Array<object> = [];
  user: User = {
  	shopname:null,
  	username:null,
  	pass:null,
  };
  constructor(public  apiService:  APIService) { }

  ngOnInit() {
  	this.getShop();
  	this.getUserAll();

  }

  	getUserAll(){
  		this.apiService.getUserAll().subscribe((data:  Array<object>) => {
         	this.userShop  =  data;
         	console.log(data);
    	});
  	}

  	public  getShop(){
    	this.apiService.getShop().subscribe((data:  Array<object>) => {
         	this.shops  =  data;
    	});
	};

	createUser(){
		console.log('work create user', this.user);
		this.apiService.createUser(JSON.stringify(this.user)).subscribe((response) => {
    		console.log(response);
				});
		this.getShop();
  	this.getUserAll();
  	this.userPanel = true;
  	this.user = {shopname:null, username:null, pass:null};
	}

}

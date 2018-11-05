import { Component, OnInit } from '@angular/core';
import {Login} from './login.model';
import {RouteModule} from '../route/route.module';
import {ActivatedRoute, Router} from '@angular/router';
import {LoginService} from '../shared/login.service';
import {APIService} from '../api.service'
 
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  
  login: Login = {
		name: "",
		pass: "" 
	};

   constructor(private loginService: LoginService,  private router: Router, private apiService:  APIService) { }

  ngOnInit() {
  }
  checkLogin(data){
     if (data['success'] == true){
       console.log("LOGIN");
        this.router.navigate(['report'])
     }
     else {
       console.log("NOT LOGIN");
     } 
     console.log(data['success']);
  }
  onClickMe() {
   
    console.log("work in login component" ,this.login.name, this.login.pass);
    // console.log(this.sharedModule.(this.login));
    //this.loginService.Login(this.login).subscribe(data => {this.checkLogin(data)});
    this.loginService.Login(this.login).subscribe(data => {console.log(data)});
    //this.clickMessage = 'You are my hero!';
  }

}

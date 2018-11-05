import { Injectable } from '@angular/core';
import {Http, Response, Headers, RequestOptions} from '@angular/http';
import { HttpClient, HttpHeaders} from  '@angular/common/http';
import { Observable } from 'rxjs';
import {RouteRoutingModule} from '../route/route-routing.module'
import { Router } from '@angular/router';
// import 'rxjs/add/operator/map';
import { map } from 'rxjs/operators';
// import { map } from 'rxjs/operato
//import {Login} from '../login/login.model'
	const ParseHeaders = {
 headers: new HttpHeaders({
  'Content-Type'  : 'application/x-www-form-urlencoded'
 })
};

@Injectable()
export class LoginService {
 constructor(private http: Http, private myRoute: Router, private httpClient:HttpClient ) { }

  // loginUsers(data) {
  // 	console.log("test POST",data)
  //   let headers = new Headers({ 'Content-Type': 'application/json' });
  //   let options = new RequestOptions({ headers: headers });
  //   let body = JSON.stringify(data);
  //   return this.http.post('/index', body, options ).map((res: Response) => res.json());
  //  }

   Login(user){
	console.log('test servise',user)
  console.log( this.http.post(`/login/`,user), 'valera');
	 return  this.http.post(`/login/`,user).pipe(map((res: Response)=> this.sendToken(res.json())));
}

  sendToken(token) {
  	// console.log("sendToken@ ", token);
  	let pars = JSON.parse(token)
    console.log(pars["rule"]);
    localStorage.setItem("m", pars['m'])
    localStorage.setItem("e", pars['e'])
    localStorage.setItem("rule", pars['rule'])
    this.myRoute.navigate(["report"]);
  }
  getToken() {
      return localStorage.getItem("rule")
  }
  isLoggednIn() {
  	//console.log("test is loged in");
    return this.getToken() !== null;
  }
  checRule(){
    if (localStorage.getItem("rule") ==="1") { 
        return true;
    } else {
      return false;
    }
  }
  logout() {
    localStorage.removeItem("rule");
    localStorage.removeItem("m");
    localStorage.removeItem("e");
    this.myRoute.navigate(["login"]);
    return  this.httpClient.delete(`/login/`,ParseHeaders).subscribe((res) => {
});
  }

}

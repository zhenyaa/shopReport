import { Injectable } from  '@angular/core';
import { HttpClient, HttpHeaders, HttpParams} from  '@angular/common/http';
	const ParseHeaders = {
 headers: new HttpHeaders({
  'Content-Type'  : 'application/x-www-form-urlencoded'
 })
};

@Injectable({
providedIn:  'root'
})

export  class  APIService {

API_URL  =  'http://localhost:5000';
constructor(private  httpClient:  HttpClient) {}

getContacts(param){
     let params: HttpParams = new HttpParams();
    Object.keys(param).forEach(function (key) {
     params = params.append(key, param[key]);
});
    return  this.httpClient.get(`/operation`, {params});
}

getOperationAll(){
    return  this.httpClient.get(`/operation`);
}

getEmitentAll(){
    return  this.httpClient.get(`/emitent`);
}

getExecuteMoneyDate(){
    return  this.httpClient.get(`/executemoney`);
}

createEmitent(username){
    console.log('test',username)
    return  this.httpClient.post(`/emitent/`,username, ParseHeaders);
}

getShop(){
    return  this.httpClient.get(`/shop`);
}
getUserAll(){
    return  this.httpClient.get(`/user`);
}

createShop(shopname){
    console.log('test',shopname)
    return  this.httpClient.post(`/shop/`,shopname, ParseHeaders);
}

createUser(username){
    console.log('test',username)
    return  this.httpClient.post(`/user/`,username, ParseHeaders);
}

createContact(operation1){
	console.log('test',operation1)
    return  this.httpClient.post(`/operation/`,operation1, ParseHeaders);
}
getAdminReport(query1){
    console.log('servis param', query1);
    // let t = [query1];
    let params: HttpParams = new HttpParams();
    Object.keys(query1).forEach(function (key) {
     params = params.append(key, query1[key]);
});
     return  this.httpClient.get(`/admin`, {params});
}


createMorning(morning){
	console.log('test',morning)
    return  this.httpClient.post(`/morning/`,morning, ParseHeaders);
}

createLastReport(report){
	console.log('test',report)
    return  this.httpClient.post(`/lastreport/`,report, ParseHeaders);
}
Login(user){
	console.log('test',user)
    return  this.httpClient.post(`/login/`,user, ParseHeaders);
}

}



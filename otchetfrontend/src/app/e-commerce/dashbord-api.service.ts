import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams} from  '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class DashbordApiService {

  constructor(private  httpClient:  HttpClient) { }

 	getSumProfit(){
    	return  this.httpClient.get(`/dashbord/summ`);
		}


	getSumInc(){
	    return  this.httpClient.get(`/dashbord/incs`);
		}

	getSumForRadar() {
	    return  this.httpClient.get(`/dashbord/rad`);
		}

	getSumForChart() {
	    return  this.httpClient.get(`/dashbord/chart`);
		}
}

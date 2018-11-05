import { Component, OnInit } from '@angular/core';
import {APIService} from '../api.service';
import { Router } from '@angular/router';
interface Morning {
	kashDesk:number
}
@Component({
  selector: 'app-morning',
  templateUrl: './morning.component.html',
  styleUrls: ['./morning.component.css']
})
export class MorningComponent implements OnInit {
kash:Morning={
   kashDesk:0
}
  constructor(private  apiService:  APIService, private myRoute: Router) { }

  ngOnInit() {
  }
  sendCash(){
  	this.apiService.createMorning(this.kash).subscribe((response) => {
    console.log(response);
    if (response['success'] = true) {
      localStorage.setItem("m", "true")
      this.myRoute.navigate(["/report/payreport"]);
    }
});
  }

}

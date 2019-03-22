import { Component, OnInit } from '@angular/core';
import {APIService} from '../api.service';
import { Router } from '@angular/router';

import { FormControl, Validators } from '@angular/forms';
//import { Observable } from 'rxjs';
//import 'rxjs/add/operator/map';
//import 'rxjs/add/operator/catch';
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
   kashDesk:null
}
public kashDeskv: FormControl;
// unamePattern = "^[0-9]+(\.[0-9]{1,2})?$";
  constructor(private  apiService:  APIService, private myRoute: Router) { }
test(v) {
  console.log(v);
}
  ngOnInit() {
 this.kashDeskv = new FormControl('', [
    Validators.required,
    Validators.minLength(1),
    Validators.pattern("^[0-9]+(\.[0-9]{1,2})?$")
  ]);
  }
  sendCash(){
  	this.apiService.createMorning(this.kash).subscribe((response) => {
    //console.log(response);
    if (response['success'] = true) {
      localStorage.setItem("m", "true")
      this.myRoute.navigate(["/report/payreport"]);
    }
});
  }

  // kashDeskv = new FormControl('',  [
  //   Validators.required,
  //   Validators.minLength(3),
  //   Validators.pattern("^[0-9]+(\.[0-9]{1,2})?$")

  //   ]);
}

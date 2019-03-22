import { Component, OnInit } from '@angular/core';
import {APIService} from '../api.service';
import { Router } from '@angular/router';
import { FormControl, Validators } from '@angular/forms';
interface LastReport{
	desk:number,
	computerDesk:number,
	notMany:number,
	liveMany:number,
}
@Component({
  selector: 'app-last-report',
  templateUrl: './last-report.component.html',
  styleUrls: ['./last-report.component.css']
})
export class LastReportComponent implements OnInit {
	lReport:LastReport = {
		desk:null,
		computerDesk:null,
		notMany:null,
		liveMany:null,
	}

  public Ldesk: FormControl;
  public LcDesk: FormControl;
  public LnMoney: FormControl;
  public LlMoney: FormControl;
  // unamePattern = "^[0-9]+(\.[0-9]{1,2})?$";
  constructor(public apiService:  APIService, public myRoute: Router) { }

  ngOnInit() {
    this.Ldesk = new FormControl('', [
    Validators.required,
    Validators.minLength(1),
    Validators.pattern("^[0-9]+(\.[0-9]{1,2})?$")
  ]);
    this.LcDesk = new FormControl('', [
    Validators.required,
    Validators.minLength(1),
    Validators.pattern("^[0-9]+(\.[0-9]{1,2})?$")
  ]);
    this.LnMoney = new FormControl('', [
    Validators.required,
    Validators.minLength(1),
    Validators.pattern("^[0-9]+(\.[0-9]{1,2})?$")
  ]);
    this.LlMoney = new FormControl('', [
    Validators.required,
    Validators.minLength(1),
    Validators.pattern("^[0-9]+(\.[0-9]{1,2})?$")
  ]);
  }

  sendReport(){
  	this.apiService.createLastReport(this.lReport).subscribe((response) => {
    console.log(response);
    if (response['success'] = true) {
      localStorage.setItem("e", "true")
      this.myRoute.navigate(["/report/payreport"]);
    }
});

  }

}

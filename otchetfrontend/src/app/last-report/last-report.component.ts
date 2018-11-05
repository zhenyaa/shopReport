import { Component, OnInit } from '@angular/core';
import {APIService} from '../api.service';
import { Router } from '@angular/router';
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
  constructor(public apiService:  APIService, public myRoute: Router) { }

  ngOnInit() {
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

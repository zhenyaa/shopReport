import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-second-menu',
  templateUrl: './second-menu.component.html',
  styleUrls: ['./second-menu.component.css']
})
export class SecondMenuComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

 getM(){
 	console.log(localStorage.getItem("m"))
 	return localStorage.getItem("m") !== "true";
 }
 getE(){
 	console.log(localStorage.getItem("e"))
 	return localStorage.getItem("e") !== "true";
 }
}

import { Component, OnInit } from '@angular/core';
import {LoginService} from '../shared/login.service'
@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {

  constructor(public auth: LoginService) { }

  ngOnInit() {
  }
showFiller = false;
mobileQuery: MediaQueryList;

}

import { Injectable } from '@angular/core';
import {Router, CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { Observable } from 'rxjs';
import {LoginService} from './shared/login.service'

@Injectable()
export class AuthGuard implements CanActivate {
  // canActivate(
  //   next: ActivatedRouteSnapshot,
  //   state: RouterStateSnapshot): Observable<boolean> | Promise<boolean> | boolean {
  //   return true;
  // }
  constructor(private loginService: LoginService, public router: Router) {};
     canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) : Observable<boolean> | boolean{
         console.log("OnlyLoggedInUsers");
          if (this.loginService.isLoggednIn()) { 
      return true;
    } else {
      window.alert("You don't have permission to view this page");
      this.router.navigate(['login']); 
      return false;
    }
    }
}

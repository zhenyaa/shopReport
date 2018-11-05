import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {LoginComponent} from '../login/login.component'
import {MorningComponent} from '../morning/morning.component'
import {PayReportComponent} from '../pay-report/pay-report.component'
import {LastReportComponent} from '../last-report/last-report.component'
import {SecondMenuComponent} from '../second-menu/second-menu.component'
import {AdminPageComponent} from '../admin-page/admin-page.component'
import {AdminShopComponent} from '../admin-shop/admin-shop.component'
import {AdminUserComponent} from '../admin-user/admin-user.component'
import {AdminReportComponent} from '../admin-report/admin-report.component'
import {AdminEmitentComponent} from '../admin-emitent/admin-emitent.component'
import {AuthGuard} from '../auth.guard'
const child2routes: Routes = [
  // { path: 'report', component: SecondMenuComponent },
  { path: 'lastreport', component: LastReportComponent },
  { path: 'payreport', component: PayReportComponent },
  { path: 'morning', component: MorningComponent },
];

const child3routes: Routes = [
  { path: 'adminreport', component: AdminReportComponent },
  { path: 'adminshop', component: AdminShopComponent },
  { path: 'adminuser', component: AdminUserComponent },
  { path: 'morning', component: MorningComponent },
  { path: 'emitent', component: AdminEmitentComponent },
];


const routes: Routes = [
  { path: 'report', component: SecondMenuComponent, children: child2routes, canActivate: [AuthGuard] },
  { path: 'admin', component: AdminPageComponent, children: child3routes,  canActivate: [AuthGuard] },
  
  { path: 'login', component: LoginComponent },
  { path: 'index', redirectTo: 'login' },
  { path: '', redirectTo: '/', pathMatch: 'full' },

];

@NgModule({
  imports: [RouterModule.forRoot(routes, {useHash: true})],
  exports: [RouterModule]
})
export class RouteRoutingModule { }

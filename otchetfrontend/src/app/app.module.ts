import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import '../polyfills';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppComponent } from './app.component';
import { MenuComponent } from './menu/menu.component';
import {SharedModule} from './shared/shared.module';
import {LoginService} from './shared/login.service';
import {LoginModule} from './login/login.module'
import { HttpModule } from '@angular/http';
import{RouteModule} from  './route/route.module'
import{RouteRoutingModule} from  './route/route-routing.module';
import { MorningComponent } from './morning/morning.component'
// import {MatNativeDateModule} from '@angular/material';
// import {MatChipsModule} from '@angular/material/chips';
import {
  //MatToolbarModule,
  MatAutocompleteModule,
  MatButtonModule,
  MatButtonToggleModule,
  MatCardModule,
  MatCheckboxModule,
  MatChipsModule,
  MatDatepickerModule,
  MatDialogModule,
  MatDividerModule,
  MatExpansionModule,
  MatGridListModule,
  MatIconModule,
  MatInputModule,
  MatListModule,
  MatMenuModule,
  MatNativeDateModule,
  MatPaginatorModule,
  MatProgressBarModule,
  MatProgressSpinnerModule,
  MatRadioModule,
  MatRippleModule,
  MatSelectModule,
  MatSidenavModule,
  MatSliderModule,
  MatSlideToggleModule,
  MatSnackBarModule,
  MatSortModule,
  MatStepperModule,
  MatTableModule,
  MatTabsModule,
  MatTooltipModule,
  

} from '@angular/material';
import {MatToolbarModule} from '@angular/material/toolbar';
import { PayReportComponent } from './pay-report/pay-report.component';
import { LastReportComponent } from './last-report/last-report.component';
import { APIService } from './api.service';
import { HttpClientModule } from '@angular/common/http'; 
import { FormsModule,ReactiveFormsModule } from '@angular/forms';
import { SecondMenuComponent } from './second-menu/second-menu.component';
import { AdminPageComponent } from './admin-page/admin-page.component';
import { AdminReportComponent } from './admin-report/admin-report.component';
import { AdminShopComponent } from './admin-shop/admin-shop.component';
import { AdminUserComponent } from './admin-user/admin-user.component';
import { MyfilterPipe } from './admin-report/myfilter.pipe';
import {CdkTableModule} from '@angular/cdk/table';
import {AuthGuard} from './auth.guard';
import { AdminEmitentComponent } from './admin-emitent/admin-emitent.component';
import { MAT_DATE_LOCALE } from '@angular/material';
import { LOCALE_ID } from '@angular/core';
@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    MorningComponent,
    PayReportComponent,
    LastReportComponent,
    SecondMenuComponent,
    AdminPageComponent,
    AdminReportComponent,
    AdminShopComponent,
    AdminUserComponent,
    MyfilterPipe,
    AdminEmitentComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    BrowserAnimationsModule,
    LoginModule,
    RouteRoutingModule,
    HttpModule,
    MatButtonModule,
    MatButtonToggleModule,
    MatCardModule,
    MatExpansionModule,
    MatListModule,
    MatInputModule,
    FormsModule,
    MatTooltipModule,
    ReactiveFormsModule,
    MatRadioModule,
    MatSelectModule,
    MatSidenavModule,
    MatDatepickerModule,
    MatNativeDateModule,
    MatTableModule,
    CdkTableModule,
    MatIconModule,
    MatToolbarModule,
    MatChipsModule
  ],
    exports: [
    RouteRoutingModule,
   ],
  providers: [LoginService, APIService, AuthGuard,{ provide: MAT_DATE_LOCALE, useValue: "ru-RU" } ],

  bootstrap: [AppComponent]
})
export class AppModule { }

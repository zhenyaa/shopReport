import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {ECommerceComponent} from './e-commerce.component';
import { ProfitCardComponent } from './profit-card/profit-card.component'

// import { NgxEchartsModule } from 'ngx-echarts';
// import { NgxChartsModule } from '@swimlane/ngx-charts';
// import { ChartModule } from 'angular2-chartjs';
// import { Chart } from 'chart.js';
import { ChartsModule } from 'ng2-charts';
import { HttpModule } from '@angular/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import {MatGridListModule} from '@angular/material/grid-list';
import {MatCardModule} from '@angular/material/card';
import {MatDividerModule} from '@angular/material/divider';
import { LesionCardComponent } from './lesion-card/lesion-card.component';
import { RadarChrtsComponent } from './radar-chrts/radar-chrts.component';
import { BarChartComponent } from './bar-chart/bar-chart.component';
import {DashbordApiService} from './dashbord-api.service'

@NgModule({
  imports: [
  MatGridListModule,
  MatCardModule,
  MatDividerModule,
  ChartsModule,
  BrowserAnimationsModule,
  HttpModule,
  BrowserModule
  ],

  declarations: [
  ECommerceComponent,
  ProfitCardComponent,
  LesionCardComponent,
  RadarChrtsComponent,
  BarChartComponent
  ],

  providers: [
  DashbordApiService
  ],

  exports: [
  ECommerceComponent, LesionCardComponent, ProfitCardComponent
],
})
export class ECommerceModule { }

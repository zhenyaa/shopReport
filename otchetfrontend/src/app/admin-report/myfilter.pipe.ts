import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'myfilter',
  pure: false
})
export class MyfilterPipe implements PipeTransform {

  transform(value: any, fil?: any): any {
  	if (value.shopname == fil){
  		console.log('its pipe', value, 'its pipe param', fil);
  		return  value
  	}

    return null;
  }

}

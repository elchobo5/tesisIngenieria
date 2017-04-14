import { Component } from '@angular/core';
import { AppService } from './app.service';

@Component({
  selector: 'my-app',
  moduleId: module.id,
  providers: [AppService], 
  templateUrl: `app.component.html`
})

export class AppComponent { 

	constructor(private appService: AppService){
  	}

	name = 'Angular';
	
	currentMenu = "inicio";
	changeMenu = (menu: any) => {
		//alert(menu + "   " + this.currentMenu);
		this.currentMenu = menu;
	} 
}

import { Component } from '@angular/core';

@Component({
  selector: 'my-app',
  moduleId: module.id,
  templateUrl: `app.component.html`
})

export class AppComponent { 

	constructor(){
  	}

	name = 'Angular';
	
	currentMenu = "inicio";
	changeMenu = (menu: any) => {
		alert(menu + "   " + this.currentMenu);
		this.currentMenu = menu;
	} 
}

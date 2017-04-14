import { Component } from '@angular/core';
import { FormsModule }   from '@angular/forms';
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
	model = {
		addOriginIp: "",
		addOriginPort: "",
		addOriginTransport: ""
        };

	changeMenu = (menu: any) => {
		//alert(menu + "   " + this.currentMenu);
		this.currentMenu = menu;
	} 
	addOrigin = () => {
		alert(this.model.addOriginIp + " " + this.model.addOriginPort+ " " +this.model.addOriginTransport);
		this.appService.addOrigin(this.model.addOriginIp, this.model.addOriginPort, this.model.addOriginTransport)
                     .subscribe(result => console.log(result));
	}
}

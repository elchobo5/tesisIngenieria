import { Component } from '@angular/core';
import { FormsModule }   from '@angular/forms';
import { AppService } from './app.service';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

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
	origins: any = [];
	model = {
		addOriginIp: "",
		addOriginPort: "",
		addOriginTransport: "",
		addSurrogateIpOrigin: "",
		addSurrogatePortOrigin: "",
		addSurrogateIpSurrogate: "",
		addSurrogatePortSurrogate: "",
		addSurrogateTransport: "",
		deleteOriginIp: "",
		deleteOriginPort: "",
		deleteOriginTransport: "",
		deleteSurrogateIpOrigin: "",
		deleteSurrogatePortOrigin: "",
		deleteSurrogateIpSurrogate: "",
		deleteSurrogatePortSurrogate: "",
		deleteSurrogateTransport: ""
        };

	changeMenu = (menu: any) => {
		//alert(menu + "   " + this.currentMenu);
		if (menu == "cdn") {
			this.getCDN();
		}
		else {
			this.currentMenu = menu;
		}
	} 
	addOrigin = () => {
		//alert(this.model.addOriginIp + " " + this.model.addOriginPort+ " " +this.model.addOriginTransport);
		this.appService.addOrigin(this.model.addOriginIp, this.model.addOriginPort, this.model.addOriginTransport)
                     .subscribe(result => { console.log(result);
					    this.model.addOriginIp = "";
					    this.model.addOriginPort = "";
					    this.model.addOriginTransport = "";
					  }
		      );
	}

	addSurrogate = () => {
		this.appService.addSurrogate(this.model.addSurrogateIpOrigin, this.model.addSurrogatePortOrigin, this.model.addSurrogateIpSurrogate, this.model.addSurrogatePortSurrogate, this.model.addSurrogateTransport)
                     .subscribe(result => { console.log(result);
					    this.model.addSurrogateIpOrigin = "";
					    this.model.addSurrogatePortOrigin = "";
					    this.model.addSurrogateIpSurrogate = "";
					    this.model.addSurrogatePortSurrogate = "";
					    this.model.addSurrogateTransport = "";
					  }
		      );
	}
	deleteOrigin = () => {

		this.appService.deleteOrigin(this.model.deleteOriginIp, this.model.deleteOriginPort, this.model.deleteOriginTransport)
                     .subscribe(result => { console.log(result);
					    this.model.deleteOriginIp = "";
					    this.model.deleteOriginPort = "";
					    this.model.deleteOriginTransport = "";
					  }
		      );
	}
	deleteSurrogate = () => {
		this.appService.deleteSurrogate(this.model.deleteSurrogateIpOrigin, this.model.deleteSurrogatePortOrigin, this.model.deleteSurrogateIpSurrogate, this.model.deleteSurrogatePortSurrogate, this.model.deleteSurrogateTransport)
                     .subscribe(result => { console.log(result);
					    this.model.deleteSurrogateIpOrigin = "";
					    this.model.deleteSurrogatePortOrigin = "";
					    this.model.deleteSurrogateIpSurrogate = "";
					    this.model.deleteSurrogatePortSurrogate = "";
					    this.model.deleteSurrogateTransport = "";
					  }
		      );
	}
	loadCDN = (data: any) => {
		//console.log(data);
		let i: any;
		let j: any;
		let surrogates: string; 
		this.origins = [];
		for (i = 0; i < data.length; i++) {
			surrogates = "";
			for (j = 0; j < data[i].surrogates.length; j++) {
				surrogates = surrogates + data[i].surrogates[j].ip + ":" + data[i].surrogates[j].port + "; ";
			}
			this.origins[i] = {'id': i, 'ip': data[i].ip, 'port': data[i].port, 'transport': data[i].transport, 'surrogates': surrogates};
		}
		console.log(this.origins);
		this.currentMenu = "cdn";
	}
	getCDN = () => {
		this.appService.getCDN()
                     .subscribe((data) => this.loadCDN(data));
	}
}

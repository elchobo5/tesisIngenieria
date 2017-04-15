import { Injectable }              from '@angular/core';
import { Http, Response, Headers, RequestOptions }          from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

@Injectable()
export class AppService {
    
  constructor (private http: Http) {}
  addOrigin = (ipOrigin: any, portOrigin: any, transportOrigin: any) => {
	let data: any = JSON.stringify({'ipOrigin': ipOrigin, 'portOrigin': parseInt(portOrigin), 'transport': transportOrigin});
        let headers: any = new Headers({ 'Content-Type': 'application/json' });
        let options: any = new RequestOptions({ headers: headers });
        let url: any = "http://localhost:3000/addOrigin";
	//console.log("LLega aca");
        return this.postRequest(url,data,options);
  }
  addSurrogate = (ipOrigin: any, portOrigin: any, ipSurrogate: any, portSurrogate:any, transport: any) => {
	let data: any = JSON.stringify({'ipOrigin': ipOrigin, 'portOrigin': parseInt(portOrigin), 'transport': transport, 'ipSurrogate': ipSurrogate, 'portSurrogate': parseInt(portSurrogate)});
        let headers: any = new Headers({ 'Content-Type': 'application/json' });
        let options: any = new RequestOptions({ headers: headers });
        let url: any = "http://localhost:3000/addSurrogate";
	//console.log("LLega aca");
        return this.postRequest(url,data,options);
  }
  deleteOrigin = (ipOrigin: any, portOrigin: any, transportOrigin: any) => {
	let data: any = JSON.stringify({'ipOrigin': ipOrigin, 'portOrigin': parseInt(portOrigin), 'transport': transportOrigin});
        let headers: any = new Headers({ 'Content-Type': 'application/json' });
        let options: any = new RequestOptions({ headers: headers });
        let url: any = "http://localhost:3000/deleteOrigin";
	//console.log("LLega aca");
        return this.postRequest(url,data,options);
  }
  deleteSurrogate = (ipOrigin: any, portOrigin: any, ipSurrogate: any, portSurrogate:any, transport: any) => {
	let data: any = JSON.stringify({'ipOrigin': ipOrigin, 'portOrigin': parseInt(portOrigin), 'transport': transport, 'ipSurrogate': ipSurrogate, 'portSurrogate': parseInt(portSurrogate)});
        let headers: any = new Headers({ 'Content-Type': 'application/json' });
        let options: any = new RequestOptions({ headers: headers });
        let url: any = "http://localhost:3000/deleteSurrogate";
	//console.log("LLega aca");
        return this.postRequest(url,data,options);
  }
  postRequest =  (url: any, data: any, options: any): Observable<any> => {
    console.log(data);
    return this.http.post(url,data,options)
                    .map(this.extractData)
                    .catch(this.handleError);
  }
  private extractData(res: Response) {
    let body = res.json();
    return body.data || { };
  }
  private handleError (error: Response | any) {
    // In a real world app, you might use a remote logging infrastructure
    let errMsg: string;
    if (error instanceof Response) {
      const body = error.json() || '';
      const err = body.error || JSON.stringify(body);
      errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
    } else {
      errMsg = error.message ? error.message : error.toString();
    }
    console.error(errMsg);
    return Observable.throw(errMsg);
  }
  
}


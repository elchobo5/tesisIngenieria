"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var http_1 = require("@angular/http");
var Observable_1 = require("rxjs/Observable");
require("rxjs/add/operator/catch");
require("rxjs/add/operator/map");
var AppService = (function () {
    function AppService(http) {
        var _this = this;
        this.http = http;
        this.addOrigin = function (ipOrigin, portOrigin, transportOrigin) {
            var data = JSON.stringify({ 'ipOrigin': ipOrigin, 'portOrigin': parseInt(portOrigin), 'transport': transportOrigin });
            var headers = new http_1.Headers({ 'Content-Type': 'application/json' });
            var options = new http_1.RequestOptions({ headers: headers });
            var url = "http://localhost:3000/addOrigin";
            //console.log("LLega aca");
            return _this.postRequest(url, data, options);
        };
        this.addSurrogate = function (ipOrigin, portOrigin, ipSurrogate, portSurrogate, transport) {
            var data = JSON.stringify({ 'ipOrigin': ipOrigin, 'portOrigin': parseInt(portOrigin), 'transport': transport, 'ipSurrogate': ipSurrogate, 'portSurrogate': parseInt(portSurrogate) });
            var headers = new http_1.Headers({ 'Content-Type': 'application/json' });
            var options = new http_1.RequestOptions({ headers: headers });
            var url = "http://localhost:3000/addSurrogate";
            //console.log("LLega aca");
            return _this.postRequest(url, data, options);
        };
        this.deleteOrigin = function (ipOrigin, portOrigin, transportOrigin) {
            var data = JSON.stringify({ 'ipOrigin': ipOrigin, 'portOrigin': parseInt(portOrigin), 'transport': transportOrigin });
            var headers = new http_1.Headers({ 'Content-Type': 'application/json' });
            var options = new http_1.RequestOptions({ headers: headers });
            var url = "http://localhost:3000/deleteOrigin";
            //console.log("LLega aca");
            return _this.postRequest(url, data, options);
        };
        this.deleteSurrogate = function (ipOrigin, portOrigin, ipSurrogate, portSurrogate, transport) {
            var data = JSON.stringify({ 'ipOrigin': ipOrigin, 'portOrigin': parseInt(portOrigin), 'transport': transport, 'ipSurrogate': ipSurrogate, 'portSurrogate': parseInt(portSurrogate) });
            var headers = new http_1.Headers({ 'Content-Type': 'application/json' });
            var options = new http_1.RequestOptions({ headers: headers });
            var url = "http://localhost:3000/deleteSurrogate";
            //console.log("LLega aca");
            return _this.postRequest(url, data, options);
        };
        this.postRequest = function (url, data, options) {
            console.log(data);
            return _this.http.post(url, data, options)
                .map(_this.extractData)
                .catch(_this.handleError);
        };
    }
    AppService.prototype.extractData = function (res) {
        var body = res.json();
        return body.data || {};
    };
    AppService.prototype.handleError = function (error) {
        // In a real world app, you might use a remote logging infrastructure
        var errMsg;
        if (error instanceof http_1.Response) {
            var body = error.json() || '';
            var err = body.error || JSON.stringify(body);
            errMsg = error.status + " - " + (error.statusText || '') + " " + err;
        }
        else {
            errMsg = error.message ? error.message : error.toString();
        }
        console.error(errMsg);
        return Observable_1.Observable.throw(errMsg);
    };
    return AppService;
}());
AppService = __decorate([
    core_1.Injectable(),
    __metadata("design:paramtypes", [http_1.Http])
], AppService);
exports.AppService = AppService;
//# sourceMappingURL=app.service.js.map
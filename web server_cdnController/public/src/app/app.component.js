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
var app_service_1 = require("./app.service");
require("rxjs/add/operator/catch");
require("rxjs/add/operator/map");
var AppComponent = (function () {
    function AppComponent(appService) {
        var _this = this;
        this.appService = appService;
        this.name = 'Angular';
        this.currentMenu = "inicio";
        this.origins = [];
        this.model = {
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
        this.changeMenu = function (menu) {
            //alert(menu + "   " + this.currentMenu);
            if (menu == "cdn") {
                _this.getCDN();
            }
            else {
                _this.currentMenu = menu;
            }
        };
        this.addOrigin = function () {
            //alert(this.model.addOriginIp + " " + this.model.addOriginPort+ " " +this.model.addOriginTransport);
            _this.appService.addOrigin(_this.model.addOriginIp, _this.model.addOriginPort, _this.model.addOriginTransport)
                .subscribe(function (result) {
                console.log(result);
                _this.model.addOriginIp = "";
                _this.model.addOriginPort = "";
                _this.model.addOriginTransport = "";
            });
        };
        this.addSurrogate = function () {
            _this.appService.addSurrogate(_this.model.addSurrogateIpOrigin, _this.model.addSurrogatePortOrigin, _this.model.addSurrogateIpSurrogate, _this.model.addSurrogatePortSurrogate, _this.model.addSurrogateTransport)
                .subscribe(function (result) {
                console.log(result);
                _this.model.addSurrogateIpOrigin = "";
                _this.model.addSurrogatePortOrigin = "";
                _this.model.addSurrogateIpSurrogate = "";
                _this.model.addSurrogatePortSurrogate = "";
                _this.model.addSurrogateTransport = "";
            });
        };
        this.deleteOrigin = function () {
            _this.appService.deleteOrigin(_this.model.deleteOriginIp, _this.model.deleteOriginPort, _this.model.deleteOriginTransport)
                .subscribe(function (result) {
                console.log(result);
                _this.model.deleteOriginIp = "";
                _this.model.deleteOriginPort = "";
                _this.model.deleteOriginTransport = "";
            });
        };
        this.deleteSurrogate = function () {
            _this.appService.deleteSurrogate(_this.model.deleteSurrogateIpOrigin, _this.model.deleteSurrogatePortOrigin, _this.model.deleteSurrogateIpSurrogate, _this.model.deleteSurrogatePortSurrogate, _this.model.deleteSurrogateTransport)
                .subscribe(function (result) {
                console.log(result);
                _this.model.deleteSurrogateIpOrigin = "";
                _this.model.deleteSurrogatePortOrigin = "";
                _this.model.deleteSurrogateIpSurrogate = "";
                _this.model.deleteSurrogatePortSurrogate = "";
                _this.model.deleteSurrogateTransport = "";
            });
        };
        this.loadCDN = function (data) {
            //console.log(data);
            var i;
            var j;
            var surrogates;
            _this.origins = [];
            for (i = 0; i < data.length; i++) {
                surrogates = "";
                for (j = 0; j < data[i].surrogates.length; j++) {
                    surrogates = surrogates + data[i].surrogates[j].ip + ":" + data[i].surrogates[j].port + "; ";
                }
                _this.origins[i] = { 'id': i, 'ip': data[i].ip, 'port': data[i].port, 'transport': data[i].transport, 'surrogates': surrogates };
            }
            console.log(_this.origins);
            _this.currentMenu = "cdn";
        };
        this.getCDN = function () {
            _this.appService.getCDN()
                .subscribe(function (data) { return _this.loadCDN(data); });
        };
    }
    return AppComponent;
}());
AppComponent = __decorate([
    core_1.Component({
        selector: 'my-app',
        moduleId: module.id,
        providers: [app_service_1.AppService],
        templateUrl: "app.component.html"
    }),
    __metadata("design:paramtypes", [app_service_1.AppService])
], AppComponent);
exports.AppComponent = AppComponent;
//# sourceMappingURL=app.component.js.map
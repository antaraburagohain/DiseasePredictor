import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class AppService {

  // http://127.0.0.1:5000/data?s1=mild_fever&s2=muscle_pain&s3=irritability&s4=depression&s5=muscle_weakness

  apiRoot = 'http://127.0.0.1:5000/data?s1=mild_fever&s2=muscle_pain&s3=irritability&s4=depression&s5=muscle_weakness';


  constructor(private http: HttpClient) { }

  getDisease(){
    return this.http.get(this.apiRoot);
  }
}

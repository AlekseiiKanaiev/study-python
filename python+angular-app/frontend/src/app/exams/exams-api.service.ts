import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Injectable} from '@angular/core';
import 'rxjs/add/operator/catch';
import {API_URL} from '../env';
import {Exam} from './exams.model';
import { Observable } from 'rxjs';

@Injectable()
export class ExamsApiService {
    constructor(private http: HttpClient) {}
    private static __handleError(err: HttpErrorResponse | any) {
        return Observable.throw(err.message || 'Error unable to complete request');
    }

    // GET list of public future events
    getExams(): Observable<Exam[]> {
        return this.http.get(`${API_URL}/exams`)
                        .catch(ExamsApiService.__handleError);
    }
}

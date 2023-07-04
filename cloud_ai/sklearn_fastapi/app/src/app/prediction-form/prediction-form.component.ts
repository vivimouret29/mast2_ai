import { Component, Input } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { PredictionService } from '../services/prediction.service';
@Component({
  selector: 'app-prediction-form',
  templateUrl: './prediction-form.component.html',
  styleUrls: ['./prediction-form.component.css']
})
export class PredictionFormComponent {
  @Input() age?: number;
  @Input() sex?: number;

  predictionResponse: string = '';
  constructor(private predictionService: PredictionService) { }

  onSubmit() {
    const data = {
      age: this.age?.toString(),
      sex: this.sex?.toString()
    };
    this.predictionService.postCandidateData(data)
      .subscribe(response => {
        this.predictionResponse = response;
        console.log(response);
      });
  }
}

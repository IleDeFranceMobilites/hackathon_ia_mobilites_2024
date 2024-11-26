import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-directions',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './directions.component.html',
  styleUrls: ['./directions.component.css']
})
export class DirectionsComponent implements OnInit {
  inputNumber: number | null = null;
  result: number | null = null;
  loading: boolean = false;
  conversationSummary: string = '';
  userDataSummary: string = '';
  optionsAndMetadata: string = '';
  message: string = '';
  intentionsEntities: string = '';

  addTwo() {
    if (this.inputNumber !== null) {
      this.loading = true;
      fetch(`http://localhost:8002/add_two/${this.inputNumber}`)
        .then(response => response.json())
        .then(data => {
          this.result = data.result;
          this.loading = false;
        })
        .catch(() => {
          this.loading = false;
          alert('Error fetching data');
        });
    }
  }

  fetchConversationSummary() {
    fetch('http://localhost:8003/summarize_conversations')
      .then(response => response.text())
      .then(data => {
        this.conversationSummary = data;
      })
      .catch(() => {
        alert('Error fetching conversation summary');
      });
  }

  fetchUserDataSummary() {
    fetch('http://localhost:8003/summarize_user_data')
      .then(response => response.text())
      .then(data => {
        this.userDataSummary = data;
      })
      .catch(() => {
        alert('Error fetching user data summary');
      });
  }

  fetchOptionsAndMetadata() {
    fetch('http://localhost:8002/options_and_metadata')
      .then(response => response.json())
      .then(data => {
        this.optionsAndMetadata = JSON.stringify(data, null, 2);
      })
      .catch(() => {
        alert('Error fetching options and metadata');
      });
  }

  fetchIntentionsEntities() {
    if (this.message.trim() !== '') {
      fetch('http://localhost:8001/get_intentions_entites', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: this.message })
      })
      .then(response => response.json())
      .then(data => {
        this.intentionsEntities = JSON.stringify(data, null, 2);
      })
      .catch(() => {
        alert('Error fetching intentions and entities');
      });
    }
  }

  ngOnInit() {
    this.fetchConversationSummary();
    this.fetchUserDataSummary();
    this.fetchOptionsAndMetadata();
  }
}
import { Component } from '@angular/core';

interface Source {
  title: string;
  url: string;
  cover_image: string;
}

const sources: Source[] = [
  {
    title: "When is Your Baby Due?",
    url: "https://www.healthhub.sg/live-healthy/when-is-your-baby-due",
    cover_image: "https://ch-api.healthhub.sg/api/public/content/8692c864101e4603868fb170c00230fe?v=534ae16e&t=livehealthyheaderimage",
  },
  {
    title: "Important Nutrients: What Should You Eat More Of?",
    url: "https://www.healthhub.sg/live-healthy/important-nutrients-what-should-you-eat-more-of",
    cover_image: "https://ch-api.healthhub.sg/api/public/content/3885d0458c0a4521beb14ca352730423?v=646204cc&t=livehealthyheaderimage",
  }
];


@Component({
  selector: 'app-source-tile',
  standalone: true,
  imports: [],
  templateUrl: './source-tile.component.html',
  styleUrl: './source-tile.component.css'
})



export class SourceTileComponent {
  sources: Source[] = [];
  
  constructor() {
    this.sources = sources;
  }
}

<template>
  <v-card class="mx-auto mt-4" max-width="96%">
    <v-card-title> 
      <v-spacer/>
      <v-spacer/>
      <v-spacer/>
      <v-text-field
        v-model="search"
        prepend-inner-icon="mdi-magnify"
        single-line
        hide-details
      />
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="items"
      :search="search"
      :items-per-page="5"
    />
  </v-card>
</template>

<script>
import axios from "axios"

export default {
  name: "Table",

  data: () => ({
    headers: [
      { text: "no", value: "no", width: "9%" },
      { text: "お店の名前", value: "store_name", width: "20%" },
      { text: "点数", value: "score", width: "10%" },
      { text: "口コミ数", value: "review_cnt", width: "12%" },
      { text: "頻出ワード", value: "text1" },
      { text: "特徴ワード", value: "text2" },
    ],
    items: [],
    search: "",
  }),
  created() {
    axios.get("/data")
    .then((response) => {
      this.items = response.data || [];
    })
    .catch((error) => {
      console.log(error);
    });
  },
}
</script>

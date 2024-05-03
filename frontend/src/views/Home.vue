<template>
  <v-container style="blue accent-1">
    <v-row class="mt-2">
      <v-col v-for="(item, i) in items" :key="i" class="d-flex mt-6" cols="12" sm="4" md="4" lg="4">
        <v-card max-width="100%" min-width="250" height="600" class="d-flex flex-column" hover >
          <v-img height="250" :src="image_path(item.image)"/>
          <v-card-title v-text="item.store_name"/>
          <v-card-text height="100%" >
            <v-row align="center" class="mx-0">
              <v-rating :value="item.score" color="amber" dense half-increments readonly size="15"/>
              <div class="grey--text ms-4">
                {{item.score}} ({{item.review_cnt}})
              </div>
            </v-row>
            <div class="text-body-2 mt-6">
              {{item.text1.slice(0, 5).join(', ')}}
            </div>
            <div class="text-body-2 mt-6">
              {{item.text2.slice(0, 5).join(', ')}}
            </div>
          </v-card-text>
          <v-spacer />
          <v-card-actions>
            <v-btn text color="teal accent-4" @click="$router.push({ name: 'Store', params: item })">
              more
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios"

export default {
  name: "Home",

  data: () => ({
    items: []
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
   methods: {
    image_path(image) {
        return "static/image/" + image;
    }
  }
}
</script>
<template>
  <v-container>
    <h1>BookFlow</h1>
    <input
      v-model="bookName"
      placeholder="Search Book"
      @input="searchBooks">
  </v-container>

  <v-list>
    <v-list-item v-for="book in books" :key="book.id">
      <v-list-item-title>{{ book.name }}</v-list-item-title>
      <v-list-item-subtitle>{{ book.author_name }}</v-list-item-subtitle>
    </v-list-item>
  </v-list>
</template>

<script>
export default {
  data() {
    return {
      bookName: "",
      books: []
    };
  },
  methods: {
    async searchBooks() {
      if (this.bookName.length > 2) {
        try {
          const response = await fetch(`http://localhost:4000/books/search?name=${this.bookName}`);
          if (!response.ok) throw new Error("Error fetching books");
          const data = await response.json();
          this.books = data.books;
        } catch (error) {
          console.error("Search failed:", error);
          this.books = [];
        }
      }
    }
  },
};
</script>

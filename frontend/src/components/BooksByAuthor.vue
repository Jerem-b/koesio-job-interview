<template>
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
            books: []
        };
    },
    props: ['authorName'],
    watch: {
    authorName(newAuthorName) {
      this.fetchBooksByAuthor(newAuthorName);
    }
  },
    methods: {
        async fetchBooksByAuthor(authorName) {
            try {
                const response = await fetch(`http://localhost:4000/books/search?author=${authorName}`);
                if (!response.ok) throw new Error("Error fetching books");
                    const data = await response.json();
                    this.books = data.books;
            } catch (error) {
                console.error("Search failed:", error);
                this.books = [];
            }
        }
    },
    mounted() {
        this.fetchBooksByAuthor();
    },
};
</script>
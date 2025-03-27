<template>
    <v-card v-for="book in books" :key="book.id" class="mx-auto ma-4" :subtitle="book.author_name" :title="book.name">
        <template v-slot:append>
            <v-icon :color="book.is_available ? 'green' : 'red'" small>
                mdi-circle
            </v-icon>
        </template>
        <v-card-text>{{ book.type }}</v-card-text>
        <v-card-actions>
            <v-btn append-icon="mdi-pen" color="orange-lighten-2" variant="text" @click="editBook(book.id)" />
            <v-btn append-icon="mdi-delete" color="red-lighten-2" variant="text" @click="deleteBook(book.id)" />
        </v-card-actions>
    </v-card>
</template>

<script>
export default {
    data() {
        return {
            books: []
        };
    },
    methods: {
        async fetchBooks() {
            try {
                const response = await fetch('http://localhost:4000/books');
                if (!response.ok) throw new Error("Error fetching books");
                const data = await response.json();
                this.books = data.books;
            } catch (error) {
                console.error("fetch books failed:", error);
                this.books = [];
            }
        },
        async deleteBook(book_id) {
            try {
                const response = await fetch(
                    `http://localhost:4000/books/${book_id}`, {
                    method: "DELETE"
                }
                );
                if (!response.ok) throw new Error("Failed to delete book");
                await response.json();
                this.books = this.books.filter(book => book.id !== book_id);
            } catch (error) {
                console.error("Error:", error);
            }
        },
        editBook(bookId) {
            this.$router.push(`/books/${bookId}`);
        }
    },
    mounted() {
        this.fetchBooks();
    }
};
</script>
<template>
    <v-container>
        <v-text-field v-model="bookName" placeholder="Search for a book..." variant="outlined" density="default"
            @update:model-value="searchBooks" style="width: 1000px;"></v-text-field>

        <v-card v-for="book in books" :key="book.id" class="mx-auto ma-4" :subtitle="book.author_name"
            :title="book.name">
            <template v-slot:append>
                <v-icon :color="book.is_available ? 'green' : 'red'" small>
                    mdi-circle
                </v-icon>
            </template>
            <v-card-text>{{ book.type }}</v-card-text>
        </v-card>
    </v-container>
</template>

<script>
export default {
    name: "SearchBook",
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
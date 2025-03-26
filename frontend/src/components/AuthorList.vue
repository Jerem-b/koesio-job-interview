<template>
    <v-list>
        <v-list-item v-for="author in authors" :key="author.id">
            <v-list-item-title class="d-flex justify-space-between align-center">
                <router-link :to="`/authors/${author.id}`" class="text-decoration-none">
                    {{ author.name }}
                </router-link>
                <v-btn v-if="!author.book_ids.length" color="red-lighten-2" icon="mdi-delete" variant="text"
                    @click="deleteAuthor(author.id)"></v-btn>
            </v-list-item-title>
            <v-list-item-subtitle>{{ author.book_ids.length }} book(s)</v-list-item-subtitle>
        </v-list-item>
    </v-list>
</template>

<script>
export default {
    data() {
        return {
            authors: []
        };
    },
    methods: {
        async fetchAuthors() {
            try {
                const response = await fetch('http://localhost:4000/authors');
                if (!response.ok) throw new Error("Error fetching authors");
                const data = await response.json();
                this.authors = data.authors;
            } catch (error) {
                console.error("fetch authors failed:", error);
                this.authors = [];
            }
        },
        async deleteAuthor(author_id) {
            try {
                const response = await fetch(
                    `http://localhost:4000/authors/${author_id}`, {
                    method: "DELETE"
                }
                );
                if (!response.ok) throw new Error("Failed to delete author");
                await response.json();
                this.authors = this.authors.filter(author => author.id !== author_id);
            } catch (error) {
                console.error("Error:", error);
            }
        }
    },
    mounted() {
        this.fetchAuthors();
    }
};
</script>
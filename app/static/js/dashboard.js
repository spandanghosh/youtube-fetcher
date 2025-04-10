class VideoDashboard {
    constructor() {
        this.currentPage = 1;
        this.initElements();
        this.bindEvents();
        this.loadVideos();
    }

    initElements() {
        this.videoGrid = document.getElementById('video-grid');
        this.searchInput = document.getElementById('search');
        this.sortSelect = document.getElementById('sort');
        this.prevBtn = document.getElementById('prev-btn');
        this.nextBtn = document.getElementById('next-btn');
        this.pageInfo = document.getElementById('page-info');
    }

    bindEvents() {
        this.searchInput.addEventListener('input', () => this.handleSearch());
        this.sortSelect.addEventListener('change', () => this.handleSort());
        this.prevBtn.addEventListener('click', () => this.handlePagination(-1));
        this.nextBtn.addEventListener('click', () => this.handlePagination(1));
    }

    async loadVideos() {
        try {
            const response = await fetch(
                `/api/videos?q=${this.searchInput.value}&sort=${this.sortSelect.value}&page=${this.currentPage}`
            );
            const data = await response.json();
            this.renderVideos(data);
        } catch (error) {
            console.error('Error loading videos:', error);
        }
    }

    renderVideos(data) {
        this.videoGrid.innerHTML = data.videos.map(video => `
            <div class="video-card">
                <img class="video-thumbnail" src="${video.thumbnail_url}" alt="${video.title}">
                <div class="video-info">
                    <h3>${video.title}</h3>
                    <p>${video.channel_title}</p>
                    <small>${new Date(video.published_at).toLocaleString()}</small>
                </div>
            </div>
        `).join('');

        this.updatePagination(data);
    }

    updatePagination(data) {
        this.pageInfo.textContent = `Page ${this.currentPage} of ${data.pages}`;
        this.prevBtn.disabled = this.currentPage <= 1;
        this.nextBtn.disabled = this.currentPage >= data.pages;
    }

    handleSearch() {
        this.currentPage = 1;
        this.loadVideos();
    }

    handleSort() {
        this.currentPage = 1;
        this.loadVideos();
    }

    handlePagination(direction) {
        this.currentPage += direction;
        this.loadVideos();
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => new VideoDashboard());
